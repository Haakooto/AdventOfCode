N = 1000
fabric = Dict{Tuple, Vector}()

for i in 1:N
    for j in 1:N
        fabric[(i, j)] = []
    end
end

claims = readlines("inputs/03")[1:end - 1]
for claim in claims
    id, _, start, size = split(claim)
    id = parse(Int, id[2:end])
    x0, y0 = parse.(Int, split(start[1:end - 1], ","))
    w, h = parse.(Int, split(size, "x"))
    for y in (y0 + 1): (y0 + h)
        for x in (x0 + 1): (x0 + w)
            append!(fabric[(y, x)], id)
        end
    end
end

cnt = 0
overlaps = Set()
free = Set()
for inch in values(fabric)
    if length(inch) > 1
        global cnt += 1
        union!(overlaps, inch)
    else
        union!(free, inch)
    end
end
println(cnt)
println(setdiff(free, overlaps))