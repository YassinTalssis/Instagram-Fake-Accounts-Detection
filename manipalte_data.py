import json
with open("insta-data/fake-v1.0/realAccountData.json",'r') as f:
    #description of data:
    #userMediaCount,mediaLikeNumbers,mediaCommentNumbers,mediaCommentsAreDisabled,
    #mediaHashtagNumbers, mediaUploadTimes,mediaHasLocationInfo,userFollowerCount
    #userFollowingCount, userHasHighlighReels,userHasExternalUrl,userTagsCount,userBiographyLength
    #usernameLength,usernameDigitCount,automatedBehaviour
    p=json.load(f)
    print(len(p))
    print(p[0])
with open("insta-data/automated-v1.0/nonautomatedAccountData.json",'r') as f:
    p=json.load(f)
    print(len(p))
    print(p[0])