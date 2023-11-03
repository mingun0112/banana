import os
import cv2
import base64
import math

skeleton_info = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [3, 5]]

def DrawObject(img,data,filter):


    img=cv2.imread(img)
    num_keypoints=data["filevalue"][0]
    keypoint_info=data["filevalue"][1]
    bbox_info=data["filevalue"][2]
    
    #cv2.rectangle(img, (int(img.shape[1]*0.05),5), (100,100), (255, 0, 0), 2)
    # print(img.shape[1],img.shape[0])

    for i in range(len(keypoint_info)):
        if filter==False:
            keypoint=keypoint_info[i]
            for k in range(2,len(keypoint), 3):
                if keypoint[k] == 2:
                    if k == 11:
                        cv2.circle(img, (keypoint[k-2], keypoint[k-1]), 6, (255, 255, 255), -1)  # 빨간색 원으로 키포인트 그리기
                    else:
                        cv2.circle(img, (keypoint[k-2], keypoint[k-1]), 6, (0, 0, 255), -1) 
            for connection in skeleton_info:
                start_point_index, end_point_index = connection
                start_point = (keypoint[(start_point_index - 1) * 3], keypoint[(start_point_index - 1) * 3 + 1])
                end_point = (keypoint[(end_point_index - 1) * 3], keypoint[(end_point_index - 1) * 3 + 1])
                if keypoint[(start_point_index - 1) * 3 + 2] == 2 and keypoint[(end_point_index - 1) * 3 + 2] == 2:
                    cv2.line(img, start_point, end_point, (0, 255, 0), 2)

            bbox=bbox_info[i]

            x, y, w, h = bbox
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 바운딩 박스 그리기

        
        if filter==True:
            cv2.rectangle(img, (int(img.shape[1]*0.05), int(img.shape[0]*0.05)), (int(img.shape[1]*0.95),int(img.shape[0]*0.95)), (255, 255, 255), 2)
            keypoint=keypoint_info[i]
            if num_keypoints[i]<4:
                continue
            if (keypoint[9] < img.shape[1]*0.05) or (keypoint[9] > img.shape[1]*0.95):
                continue
            if (keypoint[10] < img.shape[0]*0.05) or (keypoint[10] > img.shape[0]*0.95):
                continue
            else:
                for k in range(2,len(keypoint), 3):
                    if keypoint[k] == 2:
                        if keypoint[2]==2 and keypoint[5]==2:
   
                            r_pto2=(keypoint[0],keypoint[1])
                            r_pto1=(keypoint[3],keypoint[4])
                            r_V = (r_pto2[0] - r_pto1[0], r_pto2[1] - r_pto1[1])
                            r_factor_distance = 1.3
                            r_pext = (r_pto1[0] + int(r_V[0] * r_factor_distance), r_pto1[1] + int(r_V[1] * r_factor_distance))
                            r_pext_dis = int(math.sqrt((r_pto2[0] - r_pext[0]) ** 2 + (r_pto2[1] - r_pext[1]) ** 2))
                            cv2.circle(img,r_pext, r_pext_dis, (0, 255, 0), 2)
                            cv2.line(img, r_pto2, r_pext, (255, 0, 0), 2)

                        if keypoint[20]==2 and keypoint[17]==2:
                            l_pto2=(keypoint[18],keypoint[19])
                            l_pto1=(keypoint[15],keypoint[16])
                            l_V = (l_pto2[0] - l_pto1[0], l_pto2[1] - l_pto1[1])
                            l_factor_distance = 1.3
                            l_pext = (l_pto1[0] + int(l_V[0] * l_factor_distance), l_pto1[1] + int(l_V[1] * l_factor_distance))
                            l_pext_dis = int(math.sqrt((l_pto2[0] - l_pext[0]) ** 2 + (l_pto2[1] - l_pext[1]) ** 2))
                            cv2.circle(img,l_pext, l_pext_dis, (0, 255, 0), 2)
                            cv2.line(img, l_pto2, l_pext, (0, 0, 255), 2)
                        if k == 11:
                            cv2.circle(img, (keypoint[k-2], keypoint[k-1]), 6, (255, 255, 255), -1)  # 빨간색 원으로 키포인트 그리기
                        else:
                            cv2.circle(img, (keypoint[k-2], keypoint[k-1]), 6, (0, 0, 255), -1) 
                for connection in skeleton_info:
                    start_point_index, end_point_index = connection
                    start_point = (keypoint[(start_point_index - 1) * 3], keypoint[(start_point_index - 1) * 3 + 1])
                    end_point = (keypoint[(end_point_index - 1) * 3], keypoint[(end_point_index - 1) * 3 + 1])
                    if keypoint[(start_point_index - 1) * 3 + 2] == 2 and keypoint[(end_point_index - 1) * 3 + 2] == 2:
                        cv2.line(img, start_point, end_point, (0, 255, 0), 2)

                bbox=bbox_info[i]

                x, y, w, h = bbox
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 바운딩 박스 그리기


    # for k, bbox in enumerate(bbox_info):
    #     if filter==False:
    #         x, y, w, h = bbox
    #         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 바운딩 박스 그리기
    #     if filter==True:
    #         if num_keypoints[k]>3:
    #             x, y, w, h = bbox
    #             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 바운딩 박스 그리기

    # for k, keypoint in enumerate(keypoint_info):
    #     if filter==False:
    #         for i in range(2,len(keypoint), 3):
    #             if keypoint[i] == 2:
    #                 if i == 11:
    #                     cv2.circle(img, (keypoint[i-2], keypoint[i-1]), 6, (255, 255, 255), -1)  # 빨간색 원으로 키포인트 그리기
    #                 else:
    #                     cv2.circle(img, (keypoint[i-2], keypoint[i-1]), 6, (0, 0, 255), -1) 
    #         for connection in skeleton_info:
    #             start_point_index, end_point_index = connection
    #             start_point = (keypoint[(start_point_index - 1) * 3], keypoint[(start_point_index - 1) * 3 + 1])
    #             end_point = (keypoint[(end_point_index - 1) * 3], keypoint[(end_point_index - 1) * 3 + 1])
    #             if keypoint[(start_point_index - 1) * 3 + 2] == 2 and keypoint[(end_point_index - 1) * 3 + 2] == 2:
    #                 cv2.line(img, start_point, end_point, (0, 255, 0), 2)
    #     if filter==True:
    #         if num_keypoints[k] > 3:
    #             for i in range(2,len(keypoint), 3):
    #                 if keypoint[i] == 2:
    #                     if i == 11:
    #                         cv2.circle(img, (keypoint[i-2], keypoint[i-1]), 6, (255, 255, 255), -1)  # 빨간색 원으로 키포인트 그리기
    #                     else:
    #                         cv2.circle(img, (keypoint[i-2], keypoint[i-1]), 6, (0, 0, 255), -1) 
    #             for connection in skeleton_info:
    #                 start_point_index, end_point_index = connection
    #                 start_point = (keypoint[(start_point_index - 1) * 3], keypoint[(start_point_index - 1) * 3 + 1])
    #                 end_point = (keypoint[(end_point_index - 1) * 3], keypoint[(end_point_index - 1) * 3 + 1])
    #                 if keypoint[(start_point_index - 1) * 3 + 2] == 2 and keypoint[(end_point_index - 1) * 3 + 2] == 2:
    #                     cv2.line(img, start_point, end_point, (0, 255, 0), 2)






    _, buffer = cv2.imencode('.jpg', img)
    base64_string = base64.b64encode(buffer).decode("utf-8")


    return base64_string