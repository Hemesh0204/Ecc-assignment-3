
**Above folder contains codes for the project, and proof of executing the codes, have been submitted in the report. Command to run pretty much the majority of commands have been given in the report along with executed screenshots, in this readme, the code's logic would be explained.**

### Server-Side Code Logic:

1. **Initialize a port:** Initialize an port an listen/wait for connection from client
2. **Accept Connection:**  Once it receives an connection request, and client sends an message indicating to connect, it accepts it. By chance if client gets disconnected, the code will be still running, just re-executing the client would be fine.
3. **Generate and Send Data:** Now generate an random 1kb file and along with checksum being calculated, and sent to client.
4. Terminate the connection

### Client-Side Code Logic:

1. **Establish Connection:** One socket will be created and connection with server will be established using specified port number and gretting message would be sent;.
2. **Receive Data:** Gets the checksum from server, hash values will be used to indicate the end of it.
3. **Get data and write in file:** As connection being established server sends one kb file in small chunks and client starts writing this random text in the client_side.txt
4. **Verify File Integrity:** After writing the content, cleint nows calcualtes the checksum of the file, and verifies both the server side checksum which was intially recieved to be equal or not.
5. Also added 5 mins sleep before shutdown which allows us to download the file, and check it.(These is not necessary this is just for double verification step)
6. If there is an mismatch stop the process

   Note: You could say that let this loop run infinetely, untill it matches, but it is an bad idea as we dont what breaks the code, and it ends up using the all the resources, leading to total shutdown of mac, so connection would be ended, based on log values, the error could be identified, and rerurn the code.

Both the text files from server and client is also being added to the repo, so it could be verified it is the same file.

Also generated random 1kb file from the server side is also added into the repo.


### Commands to execute:

1) Create volume: docker volume create `<volume name>`
2) Build Image: docker build -t <image_name> .
3) Run the containers: docker run -d –name `<container name>` -v volume1:/volume_location -p port:port `<image-name>`
4) Calculate the checksum: docker exec -it server-container md5sum server_side.txt

Note: In while running container, we should include details of the network application if we have created it seperately, since I am using the default values, there is no need to mention it. Executing this commands in order after downloading the repo you could verify the results. Further explaination along with screenshots have been attached to the report.

Reference:

1. https://www.youtube.com/watch?v=eGz9DS-aIeY&ab_channel=NetworkChuck
2. https://www.youtube.com/watch?v=pg19Z8LL06w&ab_channel=TechWorldwithNana
3. https://www.youtube.com/watch?v=3QiPPX-KeSc&ab_channel=TechWithTim
4. https://www.youtube.com/watch?v=FGdiSJakIS4&ab_channel=freeCodeCamp.org
