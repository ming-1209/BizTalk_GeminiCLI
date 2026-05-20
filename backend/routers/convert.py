from fastapi import APIRouter, HTTPException
from backend.models.schemas import ConvertRequest, ConvertResponse
from backend.services.tone_converter import ToneConverter

router = APIRouter()
converter = ToneConverter()

@router.post("/convert", response_model=ConvertResponse)
async def convert_text(request: ConvertRequest):
    try:
        converted = await converter.convert(request.text, request.target_audience)
        return ConvertResponse(
            converted_text=converted,
            target_audience=request.target_audience,
            original_text=request.text
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM 변환 중 오류가 발생했습니다: {str(e)}")
