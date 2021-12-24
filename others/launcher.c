#include <windows.h>
#include <process.h>
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
    Sleep(8000);
    execlp("pythonw", "pythonw", "main.pyw", "test", (char*) NULL);
}
// to compile run : gcc launcher.c -o Launcher -mwindows
// Note: After compile make sure Launcher.exe is in the same directory as main.pyw