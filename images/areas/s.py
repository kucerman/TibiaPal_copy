from PIL import Image
import os


def compress_png_to_rle(png_path, out_path):
    img = Image.open(png_path).convert("1")  # force black & white
    width, height = img.size
    pixels = img.load()

    with open(out_path, "w") as f:
        for y in range(height):
            first_pixel = pixels[0, y]
            current_color = first_pixel
            start_char = "B" if current_color == 0 else "W"

            counts = []
            run_length = 1

            for x in range(1, width):
                pixel = pixels[x, y]
                if pixel == current_color:
                    run_length += 1
                else:
                    counts.append(run_length)
                    current_color = pixel
                    run_length = 1

            counts.append(run_length)

            line = start_char + ",".join(map(str, counts))
            f.write(line + "\n")


def main():
    print("PNG → Row-wise RLE compressor")
    print("Working directory:", os.getcwd())
    print()

    png_path = input("Enter input PNG path: ").strip()
    out_path = input("Enter output file path: ").strip()

    if not os.path.isfile(png_path):
        print("❌ Input file does not exist.")
        return

    try:
        compress_png_to_rle(png_path, out_path)
        print("✅ Compression completed successfully.")
        print("Output written to:", out_path)
    except Exception as e:
        print("❌ Error during processing:")
        print(e)


if __name__ == "__main__":
    main()
