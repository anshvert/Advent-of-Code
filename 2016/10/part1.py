from collections import deque, defaultdict

with open('input.txt', 'r') as f:
    instructions = f.read().splitlines()
    f.close()

Q = deque(instructions)
bot_chips_dict = defaultdict(list)
final_mn,final_mx = 17,61

while Q:
    command = Q.popleft()
    command_split = command.split(' ')
    if command_split[0] == 'value':
        bot_chips_dict[command_split[-1]].append(int(command_split[1]))
    else:
        bot_chips = bot_chips_dict[command_split[1]]
        if len(bot_chips) < 2:
            Q.append(command)
        else:
            mn,mx = min(bot_chips), max(bot_chips)
            if mn == final_mn and mx == final_mx:
                print("Final Bot", command_split[1])
                break
            if command_split[5] == 'bot':
                bot_chips_dict[command_split[6]].append(mn)
            if command_split[10] == 'bot':
                bot_chips_dict[command_split[11]].append(mx)
            bot_chips_dict[command_split[1]] = []