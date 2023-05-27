import socket

# Step 2: Implement TCP/IP communication

# City 3
def city3():
    # Send initial order message "1" to all other cities
    orders = ['1', '2', '4']
    send_orders(orders)

# Cities 1, 2, 4
def cities124(order):
    # Receive and update messages
    while True:
        message = receive_message()
        updated_message = message + order
        send_orders(updated_message)

def send_orders(orders):
    for city in ['1', '2', '4']:
        # Connect to each city's IP address and send the order
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((get_ip_address(city), 5000))
            s.sendall(orders.encode())

def receive_message():
    # Receive messages from other cities
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 5000))
        s.listen()
        conn, addr = s.accept()
        with conn:
            message = conn.recv(1024).decode()
            return message

def get_ip_address(city):
    # Return the IP address for each city
    if city == '1':
        return '192.168.0.1'
    elif city == '2':
        return '192.168.0.2'
    elif city == '3':
        return '192.168.0.3'
    elif city == '4':
        return '192.168.0.4'

# Step 6: Calculate distances and find the shortest tour
def calculate_distance(tour):
    # Define a distance matrix with distances between cities
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    total_distance = 0
    for i in range(len(tour) - 1):
        current_city = int(tour[i]) - 1
        next_city = int(tour[i + 1]) - 1
        total_distance += distance_matrix[current_city][next_city]

    return total_distance

# Step 7: Output the shortest tour
def find_shortest_tour():
    shortest_tour = None
    shortest_distance = float('inf')

    for city in ['1', '2', '3', '4']:
        # Receive final messages with tour sequences
        message = receive_message()
        tour = message + city

        distance = calculate_distance(tour)
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_tour = tour

    print("Shortest Tour:", shortest_tour)
    print("Shortest Distance:", shortest_distance)

# Step 1: Set up the Docker environment (IP addresses for each city/node)

# Step 3: Send initial order messages
city3()  # City 3 sends the initial message

# Step 4: Receive and update messages (Cities 2, 3, 4)
cities124('4')  # City 4 receives and updates messages
# Repeat the above line for City 3 and City 4, with the respective orders

# Step 5: Repeat step 4 until all cities have received and updated the messages

# Step 8: Run the function to find the shortest tour
find_shortest_tour()
