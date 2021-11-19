using PrettyTables

data = readlines("inputs/18")[1: end - 1]
# data = readlines("testinp")
N = length(data)

area = zeros(Int64, N + 2, N + 2)
for (y, row) in enumerate(data)
    for (x, acre) in enumerate(row)
        if acre == '|'
            area[y + 1, x + 1] = 1
        elseif acre == '#'
            area[y + 1, x + 1] = 10
        end
    end
end


function next_step(area)
    new_area = zeros(Int64, N + 2, N + 2)
    for y in 2:N + 1
        for x in 2:N + 1
            curr = area[y, x]
            s = sum(area[y - 1: y + 1, x - 1: x + 1]) - curr
            if curr == 0
                if s % 10 >= 3
                    new_area[y, x] = 1
                end
            elseif curr == 1
                if s >= 30
                    new_area[y, x] = 10
                else
                    new_area[y, x] = 1
                end
            else
                if (s % 10 >= 1) && (s >= 10)
                    new_area[y, x] = 10
                end
            end
        end
    end
    return new_area
end

function iterate(a, N)
    seen = Dict()
    vals = []
    for i in 1:N
        a = next_step(a)
        val = sum(a .== 1) * sum(a .== 10)
        if i == 10
            println(val)
        end
        h = hash(a)
        if h in keys(seen)
            return seen[h], i, vals
        else
            seen[h] = i
            push!(vals, val)
        end
    end
end

T = 1000000000
c0, c1, v = iterate(area, T)
vals = v[c0: c1 - 1]
println(vals[(T - c0) % (c1 - c0) + 1])
