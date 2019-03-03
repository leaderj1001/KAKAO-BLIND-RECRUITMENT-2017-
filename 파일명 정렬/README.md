# KAKAO BLIND RECRUITMENT 2017 - 파일명 정렬

## 문제 설명
- 파일명이 주어졌을 때 문제에서 제공하는 기준에 맞춰서 정렬하는 문제이다.
- 예를 들어) "img12.png"라는 input이 있을 때 중간에 있는 "12"를 기준으로 "img" -> head, "12" -> number, ".png" -> tail로 나누어 먼저 head 부분을 사전 순으로 정렬한다. 이후 head가 차이가 없다면 number 부분을 정렬하고, head와 number 부분이 같다면 먼저 들어온 순서로 정렬한다.

## 해결
- 정규식을 이용해서 데이터 전처리를 해주었고,
- 파이썬 내장 함수 sorted를 이용해서 문제를 해결하였습니다.

## 참조
[1차 파일명 정렬 문제(프로그래머스)](https://programmers.co.kr/learn/courses/30/lessons/17686)
