freqs = parse.(Int, readlines("inputs/01")[1:end - 1])
println(sum(freqs))

seen = [freqs[1]]
while !(seen[end] in seen[1:end - 1])
    new = seen[end] + freqs[length(seen) % length(freqs) + 1]
    append!(seen, new)
end
println(seen[end])

function twice(x)
    d = Dict()
    v = 0
    while true
        for i in x
            v += i
            get(d, v, 0) == 1 && return v
            d[v] = 1
        end
    end
end
println(twice(freqs))