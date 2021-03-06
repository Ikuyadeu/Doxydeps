projects <- c("egit", "egit-github", "vert.x")

for (i in 1:length(projects)) {
    project.name <- projects[i]
    print(project.name)
    project.deps <- paste(project.name, "deps.csv", sep = "/")
    project.messages <- paste(project.name, "one_message.csv", sep = "/")

    deps <- read.csv(project.deps, sep = ',', header = TRUE, row.names = NULL)

    deps$futureNo <- deps$commitNo - deps$SubNo

    messages <- read.csv(project.messages, sep = ',', header = TRUE, row.names = NULL)
    messages$message <- as.character(messages$message)
    kinds <- levels(deps$kind)
    for (kind2 in 1:length(kinds)) {
        future <- subset(deps, deps$kind == kinds[kind2])$futureNo
        #future <- subset(deps, deps$kind == kinds[kind2])$commitNo
        messages$iskind <- messages$commitNo %in% future
        write.csv(messages, paste(project.name, paste(kinds[kind2], "one_message.csv", sep = ""), sep = "/"), quote = TRUE, row.names = FALSE)
    }
}