$ErrorActionPreference = "Stop"

Set-Location $PSScriptRoot

$bundleCmd = Get-Command bundle -ErrorAction SilentlyContinue
$bundleExe = $bundleCmd.Path
$ridkExe = $null

if (-not $bundleExe) {
  $rubyInstallerBundle = Get-ChildItem -Path "C:\\Ruby*\\bin\\bundle.bat" -ErrorAction SilentlyContinue |
    Sort-Object FullName -Descending |
    Select-Object -First 1
  if ($rubyInstallerBundle) {
    $bundleExe = $rubyInstallerBundle.FullName
    $candidateRidk = Join-Path (Split-Path $bundleExe -Parent) "ridk.cmd"
    if (Test-Path $candidateRidk) {
      $ridkExe = $candidateRidk
    }
  }
}

if (-not $bundleExe) {
  Write-Error @"
Bundler not found.

1) Install Ruby (with DevKit) from https://rubyinstaller.org/
2) Open the "Start Command Prompt with Ruby" and run:
   gem install bundler -v 2.6.9
   bundle _2.6.9_ install

Then re-run: .\run_server.ps1
"@
}

$bundlerVersion = $null
if (Test-Path ".\\Gemfile.lock") {
  $lines = Get-Content ".\\Gemfile.lock"
  for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i].Trim() -eq "BUNDLED WITH") {
      if ($i + 1 -lt $lines.Count) {
        $bundlerVersion = $lines[$i + 1].Trim()
      }
      break
    }
  }
}

if (-not $ridkExe) {
  $ridkCmd = Get-Command ridk -ErrorAction SilentlyContinue
  if ($ridkCmd) {
    $ridkExe = $ridkCmd.Path
  } else {
    $ridkExe = Join-Path (Split-Path $bundleExe -Parent) "ridk.cmd"
    if (-not (Test-Path $ridkExe)) {
      $ridkExe = $null
    }
  }
}

if ($bundlerVersion) {
  try {
    if ($ridkExe) {
      & $ridkExe "exec" $bundleExe "_${bundlerVersion}_" "exec" "jekyll" "serve" "--livereload"
    } else {
      & $bundleExe "_${bundlerVersion}_" "exec" "jekyll" "serve" "--livereload"
    }
    exit 0
  } catch {
    Write-Warning "Failed to run with Bundler $bundlerVersion; falling back to default 'bundle exec'."
  }
}

if ($ridkExe) {
  & $ridkExe "exec" $bundleExe "exec" "jekyll" "serve" "--livereload"
} else {
  & $bundleExe "exec" "jekyll" "serve" "--livereload"
}
