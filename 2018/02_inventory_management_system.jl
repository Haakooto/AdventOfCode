using DataStructures

IDs = readlines("inputs/02")[1:end - 1]

function count_repeats(a)
    cnt = DefaultDict{Char, Int64}(0)
    for i in a
        cnt[i] += 1
    end
    return values(cnt)
end

function match(a, b)
    diff_idx = 0
    errs = 0
    for (k, (i, j)) in enumerate(zip(a, b))
        if i != j
            errs += 1
            diff_idx = k
        end
        if errs == 2
            return 0
        end
    end
    return diff_idx
end

twos = 0
threes = 0
for (i, ID) in enumerate(IDs)
    second_part_not_done = true

    v = count_repeats(ID)
    if 3 in v
        global threes += 1
    end
    if 2 in v
        global twos += 1
    end

    if second_part_not_done
        for other in IDs[i + 1:end]
            idx = match(ID, other)
            if idx != 0
                out = ""
                for (k, c) in enumerate(ID)
                    if k != idx
                        out *= c
                    end
                end
                println(out)
                second_part_not_done = false
            end
        end
    end
end
println(twos * threes)
