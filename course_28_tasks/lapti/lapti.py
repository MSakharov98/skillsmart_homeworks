cur_line = ''
undo_massive = [cur_line]
redo_massive = []
last_action = 0

def BastShoe(command):
    global cur_line
    global undo_massive
    global redo_massive
    global last_action
    command = list(command)

    if int(command[0]) < 1 or int(command[0]) > 5:
        return cur_line

    if command[0] == '1' or command[0] == '2':
        if last_action == 4 or last_action == 5:
            undo_massive = [cur_line]
            redo_massive = []
        cur_line = list(cur_line)
        last_action = 12
        if command[0] == '1':
            command.pop(0)
            command.pop(0)
            for i in range(len(command)):
                cur_line.append(command[i])
        else:
            command.pop(0)
            command.pop(0)
            command = ''.join(command)
            command = int(command)
            if command >= len(cur_line):
                cur_line = ''
            else:
                for i in range(command):
                    cur_line.pop(len(cur_line)-1)
        cur_line = ''.join(cur_line)
        undo_massive.append(cur_line)
        return cur_line

    if command[0] == '3':
        cur_line = list(cur_line)
        command.pop(0)
        command.pop(0)
        command = ''.join(command)
        command = int(command)
        if len(cur_line)-1 < command:
            return ''
        return cur_line[command]

    if command[0] == '4':
        last_action = 4
        if undo_massive is [] or len(undo_massive) == 1:
            return cur_line
        redo_massive.append(undo_massive[len(undo_massive)-1])
        cur_line = undo_massive[len(undo_massive)-2]
        undo_massive.pop(len(undo_massive)-1)
        return cur_line

    if command[0] == '5':
        if last_action == 12 or len(redo_massive) == 0:
            return cur_line
        else:
            last_action = 5
            undo_massive.append(redo_massive[len(redo_massive)-1])
            cur_line = redo_massive[len(redo_massive)-1]
            redo_massive.pop(len(redo_massive)-1)
            return cur_line