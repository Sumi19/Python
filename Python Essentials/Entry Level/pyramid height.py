#  write a program which reads the number of blocks the builders have,
#and outputs the height of the pyramid that can be built using these blocks.
#Note: the height is measured by the number of fully completed layers -
#if the builders don't have a sufficient number of blocks
#and cannot complete the next layer, they finish their work immediately

total_blocks=int(input("Enter Number of Blocks : "))
current_block_number=0
Height=0
while current_block_number in range (total_blocks):
    #increment height
    Height+=1
    #increase the block count by 1
    current_block_number+=1
    #get the balance blocks to work with
    total_blocks-=current_block_number
    print("We can build" ,Height, "floors")


# another way of getting the output
blocks = int(input("enter the number of blocks"))

current_blocks = 0
height = 0

while current_blocks in range(blocks):
    height += 1
    current_blocks += 1
    blocks -= current_blocks
print("The height of the pyramid:", height)

                   
