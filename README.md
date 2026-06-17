# OpenFile_win31
Call the Windows 3.1-style 'Open File' dialog.

## Win11 Native API — Fallback to comdlg32

 There is still Win3.1 'Open File' dialog resources(Template ID 1536) inside `comdlg32.dll`
 If `OFN_ENABLEHOOK` has been set, the COM-based `IFileOpenDialog` cannot approve the in-process hook, falling back to the legacy.
 Additionally, without `OFN_EXPLORER`, we can bypass Win95 style(ID 1547) too and go straightforward to Win3.1 style(ID 1536).

 # Disclaimer
 The purpose of my code is to share infos about retro computing. I don't guarntee anything about security or other issues.
 However, I don't write any malicious code, as you can see i nthe source.
 I recommend you not to use my code to build a software, especially commercial programs.

Please visit http://221.149.253.89/guestbook.php with your retro browser!
