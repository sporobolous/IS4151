from gpiozero import MCP3008

pot = MCP3008(0)

print("Program running... Press CTRL+C to exit")

try:

    while True:
        print(pot.value)

except KeyboardInterrupt:	
	print("Program terminated!")

