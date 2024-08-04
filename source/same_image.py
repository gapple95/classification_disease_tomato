import cv2

# 이미지를 로드합니다.
img1 = cv2.imread("previous_image.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("new_image.jpg", cv2.IMREAD_GRAYSCALE)

# SIFT 특징점 추출기 생성
sift = cv2.SIFT_create()

# 특징점과 디스크립터 추출
keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

# FLANN 기반 매칭
index_params = dict(algorithm=1, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(descriptors1, descriptors2, k=2)

# 좋은 매칭점만 선별
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

# 유사도 계산 (좋은 매칭점의 비율)
similarity = len(good_matches) / min(len(keypoints1), len(keypoints2))

print(f"유사도: {similarity:.2f}")

# 결과를 그립니다.
result_img = cv2.drawMatches(img1, keypoints1, img2, keypoints2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imshow("Matches", result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()