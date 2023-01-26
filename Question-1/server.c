#include<stdio.h>
#include<string.h>
#include<sys/socket.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<netinet/in.h>
#include<time.h>

int main(){
    int socketaddr, socketaddr_latest, random, x;
    struct sockaddr_in serveraddr, clientaddr;
    char buffer[200];

    socketaddr = socket(AF_INET, SOCK_STREAM, 0);
    if (socketaddr < 0){
        perror("Socket Failed");

        serveraddr.sin_family = AF_INET;
        serveraddr.stin_addr.s_addr = inet_addr("127.0.0.1");
        serveraddr.sin_port = htons(8080);

        if (bind (socketaddr, (struct sockaddr *) &serveraddr, sizeof(serveraddr)) < 0){
            perror("Bind Failed");
            listen(socketaddr, 5);

            socklen_t client_length = sizeof(clientaddr);
            socketaddr_latest = accept (socketaddr_latest, (struct sockaddr *) &clientaddr, &client_length);

            srand(time(NULL));
            random = (rand() % 900) + 100;
            sprintf(buffer, "%d", random);
            x =  write(socketaddr_latest, buffer, sizeof(buffer));

            close(socketaddr_latest);
            close(socketaddr);
            return 0;
        }
        void error(const char *alert){
            perror(alert);
            exit(1);
        }
    }
}
