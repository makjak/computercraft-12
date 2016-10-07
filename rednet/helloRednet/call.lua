rednet.open("right") --enable the modem attached to the right side of the PC
rednet.broadcast("Hello world") --send "Hello world" over rednet to all PCs in range
print("PC1 - Hello world")
id,message = rednet.receive() --wait until something is received over rednet
if id == 2 and message == "Hello from pc2" then
 write("PC2 -")
 print(message)
 rednet.send(2,"How are you") --Send a message only to the PC with ID 2
 print("PC1 - How are you")
 id,message = rednet.receive(10) --Wait until a message arrives or 10 seconds pass
 if message == "Fine thanks" then
  print("PC2 - Fine thanks")
 end
end
print("disconnecting")
rednet.close("right") --disable modem on the right side of the PC
