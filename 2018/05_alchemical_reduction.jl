polymer = readline("inputs/05")
encoded = Int.([p for p in polymer])

function react(P)
    diffs = abs.([P[i] - P[i + 1] for i in 1:length(P) - 1]) .- 32
    changed = 0 in diffs
    if changed
        new = []
        i = 1
        while i < length(P)
            if diffs[i] == 0
                i += 2
            else
                push!(new, P[i])
                i += 1
            end
        end
        if diffs[end] != 0
            push!(new, P[i])
        end
        react(new)
    else
        return length(P)
    end
end

min = length(polymer)
for c in 65:65 + 25
    enc = encoded[encoded .!= c]
    enc = enc[enc .!= c + 32]
    l = react(enc)
    if l < min
        global min = l
    end
end
println(react(encoded))
println(min)