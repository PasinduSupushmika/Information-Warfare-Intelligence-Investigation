# PowerShell Analysis and Pipeline Runner for AsteriaGrid Investigation
# Usage: powershell -ExecutionPolicy Bypass -File .\run_network_analysis.ps1

$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
$root = Split-Path -Parent $scriptPath

$dataDir = Join-Path $root "data"
$outDir = Join-Path $root "outputs"

if (-not (Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }

Write-Host "Running AsteriaGrid Network & Intelligence Pipeline..."
Write-Host "Input Directory: $dataDir"
Write-Host "Output Directory: $outDir"

$csvFile = Join-Path $dataDir "social_media_posts.csv"
$posts = Import-Csv -Path $csvFile

$nodeIds = @($posts | ForEach-Object { $_.post_id.Trim() })
$nodeCount = $nodeIds.Count
$nodeSet = New-Object 'System.Collections.Generic.HashSet[string]' (,[string[]]$nodeIds)

$edges = @()
$adjOut = @{}
$adjIn = @{}

foreach ($currNode in $nodeIds) {
    $adjOut[$currNode] = New-Object System.Collections.Generic.List[string]
    $adjIn[$currNode] = New-Object System.Collections.Generic.List[string]
}

foreach ($p in $posts) {
    $cid = $p.post_id.Trim()
    $parentRef = $p.parent_post.Trim()
    if ($parentRef -ne "" -and $nodeSet.Contains($parentRef)) {
        $edges += [PSCustomObject]@{
            parent_post_id = $parentRef
            child_post_id = $cid
            timestamp = $p.timestamp
        }
        $adjOut[$parentRef].Add($cid)
        $adjIn[$cid].Add($parentRef)
    }
}

$edges | Export-Csv -Path (Join-Path $outDir "network_edges.csv") -NoTypeInformation

# Degree
$inDegree = @{}
$outDegree = @{}
foreach ($currNode in $nodeIds) {
    $inDegree[$currNode] = $adjIn[$currNode].Count
    $outDegree[$currNode] = $adjOut[$currNode].Count
}

# Betweenness (Brandes)
$cb = @{}
foreach ($currNode in $nodeIds) { $cb[$currNode] = 0.0 }
foreach ($s in $nodeIds) {
    $S = New-Object System.Collections.Generic.Stack[string]
    $P = @{}
    $sigma = @{}
    $d = @{}
    foreach ($v in $nodeIds) {
        $P[$v] = New-Object System.Collections.Generic.List[string]
        $sigma[$v] = 0.0
        $d[$v] = -1
    }
    $sigma[$s] = 1.0
    $d[$s] = 0
    $Q = New-Object System.Collections.Generic.Queue[string]
    $Q.Enqueue($s)
    while ($Q.Count -gt 0) {
        $v = $Q.Dequeue()
        $S.Push($v)
        foreach ($w in $adjOut[$v]) {
            if ($d[$w] -lt 0) { $d[$w] = $d[$v] + 1; $Q.Enqueue($w) }
            if ($d[$w] -eq ($d[$v] + 1)) { $sigma[$w] += $sigma[$v]; $P[$w].Add($v) }
        }
    }
    $delta = @{}
    foreach ($v in $nodeIds) { $delta[$v] = 0.0 }
    while ($S.Count -gt 0) {
        $w = $S.Pop()
        foreach ($v in $P[$w]) {
            $delta[$v] += ($sigma[$v] / $sigma[$w]) * (1.0 + $delta[$w])
        }
        if ($w -ne $s) { $cb[$w] += $delta[$w] }
    }
}
$normFactor = if ($nodeCount -gt 2) { 1.0 / (($nodeCount - 1) * ($nodeCount - 2)) } else { 1.0 }

# PageRank
$alpha = 0.85
$pr = @{}
$initialPr = 1.0 / $nodeCount
foreach ($currNode in $nodeIds) { $pr[$currNode] = $initialPr }
for ($iter = 0; $iter -lt 100; $iter++) {
    $nextPr = @{}
    $danglingSum = 0.0
    foreach ($currNode in $nodeIds) {
        if ($adjOut[$currNode].Count -eq 0) { $danglingSum += $pr[$currNode] }
    }
    $base = (1.0 - $alpha) / $nodeCount + ($alpha * $danglingSum / $nodeCount)
    foreach ($currNode in $nodeIds) {
        $incomingSum = 0.0
        foreach ($inParentNode in $adjIn[$currNode]) {
            $incomingSum += $pr[$inParentNode] / $adjOut[$inParentNode].Count
        }
        $nextPr[$currNode] = $base + ($alpha * $incomingSum)
    }
    $diff = 0.0
    foreach ($currNode in $nodeIds) { $diff += [Math]::Abs($nextPr[$currNode] - $pr[$currNode]) }
    $pr = $nextPr
    if ($diff -lt 1e-7) { break }
}

$postsMap = @{}
foreach ($p in $posts) { $postsMap[$p.post_id.Trim()] = $p }
$nodeRecords = @()
foreach ($currNode in $nodeIds) {
    $p = $postsMap[$currNode]
    $nodeRecords += [PSCustomObject]@{
        post_id = $currNode
        account = $p.account
        channel = $p.channel
        in_degree = $inDegree[$currNode]
        out_degree = $outDegree[$currNode]
        total_degree = ($inDegree[$currNode] + $outDegree[$currNode])
        betweenness = [Math]::Round($cb[$currNode] * $normFactor, 6)
        pagerank = [Math]::Round($pr[$currNode], 6)
        repost_count = [int]$p.repost_count
        reply_count = [int]$p.reply_count
        image_id = $p.image_id
    }
}

$nodeRecords | Sort-Object out_degree, pagerank -Descending | Export-Csv -Path (Join-Path $outDir "network_nodes.csv") -NoTypeInformation

$timelineRecords = $posts | Sort-Object timestamp | ForEach-Object {
    [PSCustomObject]@{
        timestamp_original = $_.timestamp
        timestamp_utc = ([DateTime]::Parse($_.timestamp)).ToUniversalTime().ToString("yyyy-MM-dd HH:mm:ssZ")
        post_id = $_.post_id
        account = $_.account
        channel = $_.channel
        parent_post = $_.parent_post
        repost_count = $_.repost_count
        reply_count = $_.reply_count
        image_id = $_.image_id
        text = $_.text
    }
}
$timelineRecords | Export-Csv -Path (Join-Path $outDir "timeline.csv") -NoTypeInformation

Write-Host "Pipeline execution complete! Generated files:"
Write-Host " - $(Join-Path $outDir 'network_edges.csv')"
Write-Host " - $(Join-Path $outDir 'network_nodes.csv')"
Write-Host " - $(Join-Path $outDir 'timeline.csv')"
