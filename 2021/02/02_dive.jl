lines = readlines("inputs/02")

function p1()
    pos = [0, 0]
    for line in lines
        dir, cnt = split(line, " ")
        if dir[1] == 'f'
            pos[1] += parse(Int, cnt)
        elseif dir[1] == 'd'
            pos[2] += parse(Int, cnt)
        else
            pos[2] -= parse(Int, cnt)
        end
    end
    println(prod(pos))
end
function p2()
    pos = [0, 0]
    aim = 0
    for line in lines
        dir, cnt = split(line, " ")
        cnt = parse(Int, cnt)
        if dir[1] == 'f'
            pos[1] += cnt
            pos[2] += aim * cnt
        elseif dir[1] == 'd'
            aim += cnt
        else
            aim -= cnt
        end
    end
    println(prod(pos))
end

p1()
p2()