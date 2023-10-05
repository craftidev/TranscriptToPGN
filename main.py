print("enter timestamp in integer minutes\n\n")

raw_input = input("enter the pgn:\n\n")

no_break = raw_input.replace('\n', ' ').replace('\r', '')
clean_start = no_break[no_break.find('1. '):]
temp_space = clean_start.replace('. ', '..')
clk = temp_space.replace(' ', ' { [%clk 00:00:00] } ')

splited = clk.split()

def Convert_timestamp(timestamp):
	timestamp = int(timestamp)
	if timestamp == 0:
		return('00:00:30]')
	else:
		hours = timestamp // 60
		minutes = timestamp % 60
		hours = str(hours)
		minutes = str(minutes)
		
		return(':'.join([hours.zfill(2), minutes.zfill(2), '00]']))
		

for chunk in splited:
	if ".." in chunk:
		move_num = chunk[:chunk.index("..") + len("..")][:2]
		turn = "White"
	if chunk == '00:00:00]':
		timestamp = input("Timestamp for " + turn + " at move n°" + move_num + "?\n")
		splited[splited.index(chunk)] = Convert_timestamp(timestamp)
		turn = "Black"

string = ' '.join(splited)
final_result = string.replace('..', '. ')

print(final_result)
