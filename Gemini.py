class GeminiContent:
    response_id: str
    item_id: str
    output_index: int
    content_index: int
    text: str
    audio: list[rtc.AudioFrame]
    text_stream: AsyncIterable[str]
    audio_stream: AsyncIterable[rtc.AudioFrame]
    content_type: Literal["text", "audio"]