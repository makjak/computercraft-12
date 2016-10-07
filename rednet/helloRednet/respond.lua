rednet.open("right") --enable modem on the right side of the PC
id,message = rednet.receive() --wait until a mesage is received
if id == 1 and message == "Hello world" then
 rednet.send(1,"Hello from pc2") -- send a message to only the PC with ID 1
 id,message = rednet.receive() -- Wait until a message is received
 if message == "How are you" then
  rednet.broadcast("Fine thanks") -- Send to all PCs in range
 end
end
rednet.close("right") -- disable modem on the right side of the PC
