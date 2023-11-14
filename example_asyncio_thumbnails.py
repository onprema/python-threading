import asyncio
import random

async def handle_requests():
    print('handling a request...')
    await asyncio.sleep(random.randint(0,3))
    print('finished handling a request')


async def generate_thumbnail(input_path, output_path):
    command = f'convert {input_path} -thumbnail 100x100 {output_path}'
    await asyncio.sleep(1) # fake delay
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    _, stderr = await process.communicate()

    if process.returncode == 0:
        print(f"Thumbnail generated successfully: {output_path}")
    else:
        print(f"Thumbnail generation failed. Error: {stderr.decode()}")

async def handle_uploaded_image(file_path):
    # Assuming file_path is the path to the uploaded image
    print('handling an image...')
    thumbnail_path = file_path.replace('.', '_thumb.')

    # Generate thumbnail asynchronously
    await generate_thumbnail(file_path, thumbnail_path)

# Example usage
while True:
    asyncio.run(handle_requests())
    has_image = random.randint(1,3) == 2
    if has_image:
        asyncio.run(handle_uploaded_image('tree.png'))
