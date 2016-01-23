library(ggplot2)

hashtags <- read.csv("/home/deepak/nltk_data/dengue_fuzzy/data/hash.tag.counts.csv", header=T)

#quartz()
top.hashtags <- subset(hashtags, hash.tag %in% c("dengue", "ondox", "brazil", "ebola", "health", "mosquito"))
ggplot(top.hashtags, aes(x=count)) + geom_freqpoly(aes(group=hash.tag, colour=hash.tag)) + theme(axis.text.x=element_text(angle=-90, hjust=0, size=10))
ggplot.save()
ggplot(top.hashtags, aes(x=top.hashtags)) + geom_freqpoly(aes(group=hash.tag, colour=hash.tag)) + theme(axis.text.x=element_text(angle=-90, hjust=0, size=10))
ggplot.save()