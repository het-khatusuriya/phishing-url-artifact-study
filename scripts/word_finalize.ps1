# Update TOC/fields in the generated .docx with Microsoft Word and export a PDF copy.
param([string]$Docx)
$full = (Resolve-Path $Docx).Path
$pdf = [System.IO.Path]::ChangeExtension($full, ".pdf")
$w = New-Object -ComObject Word.Application
$w.Visible = $false
$d = $w.Documents.Open($full)
$d.Fields.Update() | Out-Null
foreach ($t in $d.TablesOfContents) { $t.Update() }
$d.Save()
$d.ExportAsFixedFormat($pdf, 17)
"pages: " + $d.ComputeStatistics(2)
$d.Close()
$w.Quit()
"pdf: " + $pdf
