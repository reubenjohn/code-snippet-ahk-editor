#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
#SingleInstance Force
SendMode Event  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

rand_gaussian(mean, standard_deviation)
{
	max_random = 10000000
	Random, r1, 1, max_random ; 1 to prevent inf error
	Random, r2, 1, max_random
	Return mean + standard_deviation * Sqrt(-2 * Ln(r1 / max_random)) * Cos(2 * 3.14159265 * (r2 / max_random))
}
