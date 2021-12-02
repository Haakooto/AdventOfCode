depths = parse.(Int, readlines("inputs/01")[1:end-1])

increases = [(depths[i] > depths[i - 1]) for i in 2:length(depths)]
println(sum(increases))

convolved = [sum(depths[i:i+2]) for i in 1:length(depths) - 2]
convolved_incs = [(convolved[i] > convolved[i - 1]) for i in 2:length(convolved)]
println(sum(convolved_incs))