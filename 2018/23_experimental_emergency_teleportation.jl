using DataStructures


struct Bot
    id::Int
    pos::Vector{Int}
    r::Int
end

function build_bots(bots)
    swarm = []
    id = 0
    for bot in bots
        id += 1
        start = findfirst('<', bot)
        stop = findfirst('>', bot)
        rad = findlast('=', bot)
        pos = bot[start + 1: stop - 1]
        pos = parse.(Int, split(pos, ','))
        r = bot[rad + 1: end]
        r = parse(Int, r)
        push!(swarm, Bot(id, pos, r))
    end
    return swarm
end

function larget_radius(swarm)
    rad = 0
    best_bot = 0
    for bot in swarm
        if bot.r > rad
           best_bot = bot
           rad = bot.r
        end
    end
    return best_bot
end

function in_range(here, bot::Bot)
    return sum(abs.(bot.pos .- here)) < bot.r
end

function bot_coverage(bot)
    X, Y, Z = [bot.pos[i] for i in 1:3]
    r = bot.r
    P = []
    for x in X - r: X + r
        for y in Y - r: Y + r
            for z in Z - r: Z + r
                p = (x, y, x)
                if in_range(p, bot)
                    push!(P, p)
                end
            end
        end
    end
    return P
end

function swarm_coverage(swarm)
    coverage = DefaultDict{Tuple{Int}, Int}(0)
    for (i, bot) in enumerate(swarm)
        print(i, " ")
        cov = bot_coverage(bot)
        for p in cov
            coverage[p] += 1
        end
    end
    return coverage
end

function main()
    bots = readlines("inputs/23")[1: end - 1]
    # bots = readlines("testinp")
    swarm = build_bots(bots)
    alpha_bot = larget_radius(swarm)
    println(sum([in_range(bot.pos, alpha_bot) for bot in swarm]))
    coverage = swarm_coverage(swarm)
end

main()