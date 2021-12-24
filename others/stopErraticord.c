#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/types.h>
#include <processthreadsapi.h>


int main() {
    char temp[128];

    // - -- --- < - > --- -- -
    FILE* uname = popen("echo \%username%", "r");
    char* cmd = (char*)malloc(512 * sizeof(char));
    char result[24]={0x0};
    while (fgets(result, sizeof(result), uname) !=NULL){
        result[strcspn(result, "\n")] = 0;
        sprintf(cmd, "C:/Users/%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Launcher.exe.lnk", result);
    }
    pclose(uname);
    // - -- --- < - > --- -- -
    // --- --- get pid --- -- - >
    char pid_s[20];
    FILE *fptr;
    if ((fptr = fopen("pid.txt", "r")) == NULL) {
        printf("[!] Error Opening pid.txt");
        exit(1); // Exit if pointer returns NULL
    }
    fscanf(fptr, "%[^\n]", pid_s);
    fclose(fptr);
    char* process_cmd = (char*)malloc(512 * sizeof(char));
    sprintf(process_cmd, "taskkill /F /PID %s", pid_s);
    // printf("%s\n", process_cmd);

    // - -- --- < - > --- -- -
    int choice;
    Menu:
    printf("Choose: \n1- Pause Erraticord until restart: \n2- Disable startup\n >> ");
    if (fgets(temp, sizeof(temp), stdin) != NULL) {
        int test;
        if(sscanf(temp, "%d", &test) == 1){
            choice = test;
        } else{
            puts("Expected a number not characters! please try again.");
            goto Menu;
        }
    }

    switch (choice) {
        case 1:
            system(process_cmd);
            printf("[>] Process with Id: %s terminated", pid_s);
            char enter2 = 0;
            while (enter2 != '\r' && enter2 != '\n') { enter2 = getchar(); }
            break;
        case 2:

            if (remove(cmd) == 0) {
                printf("[>] Successfully removed from startup |> It won't launch automatically anymore...");
            } else {
                printf("[!] Unable to disable startup, please try deleting manually");
            }
            puts("[>] Successfully removed from startup |> It won't launch automatically anymore...");
            printf("[>] Press enter to continue\n");
            free(cmd);
            char enter = 0;
            while (enter != '\r' && enter != '\n') { enter = getchar(); }
            break;
    }   




    return 0;
}

