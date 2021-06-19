#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Set working dir to current script dir

z::
{
    loop{
        Send {CtrlDown}+{Numpad2 Down}
        sleep 30
        Send {CtrlUp}+{Numpad2 Up}
        sleep 15000
        Send {CtrlDown}+{Numpad3 Down}
        sleep 30
        Send {CtrlUp}+{Numpad3 Up}
        sleep 15000
    }
}

esc::ExitApp