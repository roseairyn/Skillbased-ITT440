#include<stdio.h>
#include<string.h>
#include<sys/socket.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<netinet/in.h>
#include<time.h>

int main(){
    int socketaddr, x;
    struct sockaddr_in serveraddr;
    char buffer[200];

    socketaddr = socket(AF_INET, SOCK_STREAM, 0);
    if (socketaddr < 0)
        perror("Socket Failed");

        serveraddr.sin_family = AF_INET;
        serveraddr.stin_addr.s_addr = inet_addr("127.0.0.1");
        serveraddr.sin_port = htons(8080);

        if (connect (socketaddr, (struct sockaddr *) &serveraddr, sizeof(serveraddr)) < 0)
            perror("Connection Failed");

            (buffer, sizeof(buffer));
            x = read(socketaddr, buffer, sizeof(buffer) - 1);

            if (x < 0)
                perror("Socket reading error");
                printf("Random number generated: %s\n", buffer);

                close(socketaddr);
                return 0;  
}
    void error(const char *alert){
        perror(alert);
        exit(1);
    }
    