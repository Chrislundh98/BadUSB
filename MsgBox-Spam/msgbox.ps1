Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

$leftCtrlPressed = $false
$rightCtrlPressed = $false

$onKeyDown = [System.Windows.Forms.KeyEventHandler]{
    Param($sender, $e)

    if ($e.KeyCode -eq [System.Windows.Forms.Keys]::ControlKey) {
        if ($e.KeyData -band [System.Windows.Forms.Keys]::LControlKey) {
            $leftCtrlPressed = $true
        }
        elseif ($e.KeyData -band [System.Windows.Forms.Keys]::RControlKey) {
            $rightCtrlPressed = $true
        }
    }

    if ($leftCtrlPressed -and $rightCtrlPressed) {
        Start-Sleep -Seconds 5  # Wait for 5 seconds to check if both keys are still pressed.
        if ($leftCtrlPressed -and $rightCtrlPressed) {
            Get-Process | Where-Object {$_.ProcessName -eq 'msgbox'} | Stop-Process
            $leftCtrlPressed = $false
            $rightCtrlPressed = $false
        }
    }
}

$onKeyUp = [System.Windows.Forms.KeyEventHandler]{
    Param($sender, $e)

    if ($e.KeyCode -eq [System.Windows.Forms.Keys]::ControlKey) {
        $leftCtrlPressed = $false
        $rightCtrlPressed = $false
    }
}

class MyMessageFilter implements [System.Windows.Forms.IMessageFilter] {
    [bool] PreFilterMessage([ref] [System.Windows.Forms.Message] $m) {
        $WM_KEYDOWN = 0x100
        $WM_KEYUP = 0x101

        if ($m.Msg -eq $WM_KEYDOWN) {
            $onKeyDown.Invoke($null, [System.Windows.Forms.KeyEventArgs]::new($m.WParam))
        }
        if ($m.Msg -eq $WM_KEYUP) {
            $onKeyUp.Invoke($null, [System.Windows.Forms.KeyEventArgs]::new($m.WParam))
        }
        return $false
    }
}

$form = New-Object System.Windows.Forms.Form
$form.WindowState = 'Minimized'
$form.ShowInTaskbar = $false

$hook = New-Object System.Windows.Forms.NativeWindow
$hook.AssignHandle((Get-Process -Id $pid).MainWindowHandle)
$filter = [MyMessageFilter]::new()
[System.Windows.Forms.Application]::AddMessageFilter($filter)

# Run the application message loop
[System.Windows.Forms.Application]::Run($form)
