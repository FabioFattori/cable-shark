import socket
import struct
import select
import time
import requestResponsens

def ping_ip(ip_address):
    # Controlla se l'indirizzo IP è valido
    try:
        socket.inet_aton(ip_address)
    except socket.error:
        return (requestResponsens.res.get(3),"Indirizzo IP non valido")

    # Imposta un timeout per la ricezione della risposta
    timeout = 5
    
    # Crea un socket UDP
    icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_ICMP)
    
    # Costruisci il pacchetto ICMP echo request
    header = struct.pack("!BBHHH", 8, 0, 0, 1, 1)
    data = b"Hello World!"
    checksum = calculate_checksum(header + data)
    header = struct.pack("!BBHHH", 8, 0, checksum, 1, 1)
    packet = header + data

    try:
        # Invia il pacchetto ICMP echo request
        icmp_socket.sendto(packet, (ip_address, 1))
        
        # Aspetta la risposta
        start_time = time.time()
        ready = select.select([icmp_socket], [], [], timeout)
        icmp_socket.close()
        if ready[0]:
            #response, addr = icmp_socket.recvfrom(1024)
            end_time = time.time()
            return (requestResponsens.res.get(1),f"Ping riuscito verso {ip_address} (Tempo di risposta: {round((end_time - start_time) * 1000, 2)} ms)")
        else:
            return (requestResponsens.res.get(0),f"Timeout scaduto durante il ping verso {ip_address}")
    except socket.error as e:
        icmp_socket.close()
        return (requestResponsens.res.get(3),f"Errore durante il ping verso {ip_address}: {str(e)}")
        

def calculate_checksum(data):
    # Calcola la checksum del pacchetto ICMP
    sum = 0
    count_to = (len(data) // 2) * 2
    count = 0
    while count < count_to:
        this_val = data[count+1] * 256 + data[count]
        sum = sum + this_val
        sum = sum & 0xffffffff
        count = count + 2

    if count_to < len(data):
        sum = sum + data[len(data) - 1]
        sum = sum & 0xffffffff

    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer