#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
下载Sketchfab龙模型的脚本
"""
import webbrowser
import os

# 模型信息
MODEL_URL = "https://sketchfab.com/3d-models/dragon-rigged-eb958a6e66f542cbb1cbabc4d36f34d9"
MODEL_NAME = "Dragon Rigged"

print("=" * 60)
print(f"准备下载: {MODEL_NAME}")
print("=" * 60)
print()
print("下载步骤：")
print("1. 浏览器将打开模型页面")
print("2. 点击页面上的 'Download 3D Model' 按钮")
print("3. 如果需要登录，可以使用Google/Facebook快速登录")
print("4. 选择 GLB 或 FBX 格式下载")
print("5. 下载完成后，将文件放到当前目录")
print()
print("推荐格式: GLB (最兼容)")
print()

input("按回车键打开浏览器...")

# 打开浏览器
webbrowser.open(MODEL_URL)

print()
print("浏览器已打开！")
print("下载完成后，将文件重命名为 'dragon.glb' 并放到此目录")
print(f"当前目录: {os.getcwd()}")
