import pytest

from playwright.sync_api import Page, expect

def test_frames(page :Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    # frame1 = page.frame(url= "https://ui.vision/demo/webtest/frames/frame_1")
    # frame_1 = frame1.locator("input[type='text']")
    # frame_1.fill("Welcome")
    # expect(frame_1).to_have_value("Welcome")

    frame3 = page.frame(url = "https://ui.vision/demo/webtest/frames/frame_3")
    frame_3 = frame3.locator("input[type='text']")
    frame_3.fill("Welcome")

    child_frames = frame3.child_frames
    print("Total child frames",len(child_frames))

    inner_frame = child_frames[0]
    inner_frame.get_by_label("I am a human").check()





