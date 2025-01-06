import requests, argparse, os


def main() -> None:
    parser = argparse.ArgumentParser(
        description="A CLI tool for gaining inspiration for college supplementals. Do NOT submit these generated essays to colleges."
    )
    parser.add_argument(
        "-q", "--question", help="The college supplemental prompt.", required=True
    )
    parser.add_argument(
        "-p",
        "--profile",
        help="The .vcl file containing your facts about you.",
        required=True,
    )
    parser.add_argument(
        "-wc",
        "--word-count",
        type=int,
        help="The max word count for the question. The LLM will attempt to create an essay using as many words as possible.",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="The file where the response should be saved.",
        required=True,
    )
    args = parser.parse_args()

    if not os.path.exists(args.profile):
        print(
            "You provided an invalid path for the profile flag. Try providing the absolute path to the profile."
        )
        return

    if not args.profile.endswith("vcl"):
        print("Please provide a vcl file. For example: 'profile.vcl'.")
        return

    file_contents = ""
    with open(args.profile) as f:
        file_contents = f.read()

    GEMINI_URL = f"""
    https://nova-motors-server.vercel.app/gemini?prompt=
Create an college supplemental essay response for the prompt, break it up into multiple paragraphs: {args.question}
The question has a max word count of {args.word_count}, and you will attempt to use as many words as possible.
Here are some facts regarding the student, please try to use them all in the essay: \n{file_contents}
    """

    print(
        "Calling Google Gemini now. Please note that since I'm hosting my Flask app on Vercel, there might be a cold start, so this may take a while.\n"
    )
    response = requests.get(GEMINI_URL).json()

    print("The response is saved to the output file.")

    with open(args.output, "w") as f:
        print(response["candidates"][0]["content"]["parts"][0]["text"], file=f)


if __name__ == "__main__":
    main()
