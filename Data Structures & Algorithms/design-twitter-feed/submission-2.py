from collections import defaultdict
class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = list()


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        recent_tweets = list()
        for i in range(len(self.tweets) -1, -1, -1):
            user_id, tweet_id = self.tweets[i]
            if user_id == userId or user_id in self.users[userId]:
                recent_tweets.append(tweet_id)
                if len(recent_tweets) == 10:
                    break
        return recent_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)
