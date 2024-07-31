@("C:\SourceFolder\file1.txt", "C:\SourceFolder\file2.txt", "C:\SourceFolder\file3.txt") | ForEach-Object { Move-Item -Path $_ -Destination "C:\DestinationFolder" }
