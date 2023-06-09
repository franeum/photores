import time
import wifi
import socketpool
import board
import analogio

N_SAMPLES = 8
samples = [0] * N_SAMPLES
counter = 0

HOST = "192.168.1.132"
PORT = 5005
adc = analogio.AnalogIn(board.D33)
pool = socketpool.SocketPool(wifi.radio)
sock = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)

while True:
    try:
        samp = adc.value
        samples[counter] = samp
        avg = sum(samples) / N_SAMPLES
        udp_message = bytes(f"{avg}", 'utf-8')
        sock.sendto(udp_message, (HOST, PORT))
        counter += 1

        if counter >= N_SAMPLES:
            counter = 0

    except KeyboardInterrupt:
        print("INTERRUPTED")
        break

    time.sleep(0.25)
