import json
import requests
import os

def unstable(title, guide_being, image):
    url = 'https://stablediffusionapi.com/api/v3/text2img'
    headers = {'Content-Type': 'application/json'}
    api_key = "X9BMj9TeT1TgCJElOM3PzootCWrBdg0oLEJUTBDDT7R3F1MvtEYIsGPgoTej"
    data = {
        "key": api_key,
        "prompt": f'{image}',
        "negative_prompt": "deformed, blurry, bad anatomy, disfigured, poorly drawn features, mutation, mutated, extra limbs, ugly, poorly drawn paws or claws, messy drawing, broken limbs, low res, bad proportions, bad shadow, uncoordinated body, unnatural body, poorly drawn fur or feathers, missing body parts, disproportionate body parts, bad ears, poorly drawn ears, extra ears, missing ears, old photo, black and white, black and white filter, colorless, distorted perspective, inaccurate shading, incorrect lighting, lack of depth, unbalanced composition, lack of detail, exaggerated features, inconsistent style, incorrect proportions, awkward posing, floating limbs, incomplete drawing, uneven textures, rough edges, pixelated image, repeating or tiling edges, mismatched features, hybrid animals, mixed species, multiple animals in a single portrait, extra heads, extra sets of limbs, extra eyes, anatomical inconsistencies, fussy.",
        "width": "720",
        "height": "720",
        "samples": "1",
        "num_inference_steps": "35",
        # "seed": null,
        "guidance_scale": 7.5,
        "safety_checker":"yes",
        # "webhook": null,
        # "track_id": null
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()

    if response_json["status"] == "success":
        image_url = response_json["output"][0]
        image_response = requests.get(image_url)

        # Save the image
        output_directory = f'/content/drive/MyDrive/yetiChat/out/{title}/image'
        os.makedirs(output_directory, exist_ok=True)

        with open(f'{output_directory}/{guide_being}.jpg', 'wb') as image_file:
            image_file.write(image_response.content)

        # Save the JSON response
        with open(f'{output_directory}/{guide_being}.json', 'w') as json_file:
            json.dump(response_json, json_file)
    else:
        print(f"Error generating image: {response_json['error']}")
        print(f'Full stableAPI Repsonse {response_json}')