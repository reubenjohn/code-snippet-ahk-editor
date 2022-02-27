#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
#SingleInstance Force
SendMode Event  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#Include rand_gaussian.ahk
#Include java/println.ahk
#Include java/println_format.ahk

mean := 311 / 4
std = 152 / 4

!Escape::abort_typing_code_snippet()
^!i::match_shortcut(mean, std)

match_shortcut(mean, std) {
    Input userKeys, L2
    switch (userKeys) {
        case "pl": type_code_snippet_println(mean, std) return
        case "pf": type_code_snippet_println_format(mean, std) return
    }
}

abort_typing_code_snippet() {
    Send, {Shift Up}
    Send, {Ctrl Up}
    Send, {Alt Up}
    Reload
}