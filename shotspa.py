from playwright.sync_api import sync_playwright
scr=[("dashboard","dashboard"),("fleet","fleet"),("trailers","trailers")]
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={"width":1280,"height":760}, device_scale_factor=1)
    pg.goto("file://"+__import__('os').path.abspath("index.html"))
    pg.wait_for_timeout(500)
    for sid,name in scr:
        pg.evaluate(f"show('{sid}')")
        pg.wait_for_timeout(300)
        pg.screenshot(path=f"spa_{name}.png")
    b.close()
    print("done")
