# Fake_Accounts_Classifier_In_Instagram
This work inspired by the following paper: [Intagram Fake and Automated Account Detection](https://arxiv.org/pdf/1910.03090.pdf)

[dataset link](https://github.com/fcakyon/instafake-dataset/tree/master/data/fake-v1.0)

### Dataset Structures

The dataset contains of 2 set of json files with given features:

##### Fake Account Detection
1. `user_media_count` - Total number of posts, an account has.
2. `user_follower_count` - Total number of followers, an account has.
3. `user_following_count` - Total number of followings, an account has.
4. `user_has_profil_pic` - Whether an account has a profil picture, or not.
5. `user_is_private` - Whether an account is a private profile, or not.
6. `user_biography_length` - Number of characters present in account biography.
7. `username_length` - Number of characters present in account username.
8. `username_digit_count` - Number of digits present in account username.
9. `is_fake` - True, if account is a spam/fake account, False otherwise
