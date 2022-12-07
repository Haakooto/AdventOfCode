data = readlines("04")

rand_nums = parse.(Int, split(data[1], ','))

puzzles = []
won = []
for k in 3:6:length(data)
    a = reshape(vcat([parse.(Int, split(data[i], ' ', keepempty=false)) for i in k:k+4]...), 5, 5)
    push!(puzzles, a)
end

function bingo()
    for num in rand_nums
        for p in puzzles
            if !(p in won)
                if num in p
                    p[findall(x->x==num, p)] .= 100
                    if 0 in sum(p .!== 100, dims=1) || 0 in sum(p .!== 100, dims=2)
                        if length(won) in [0, length(puzzles) - 1]
                            println(sum(p[p .!== 100]) * num)
                        end
                        push!(won, p)
                    end
                end
            end
        end
    end
end

bingo()