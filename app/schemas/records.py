from pydantic import BaseModel, Field

class LoginInput(BaseModel):
    username: str
    password: str

class ChildInput(BaseModel):
    child_code: str
    name: str
    age_months: int = Field(ge=0, le=60)
    sex: str

class VisitInput(BaseModel):
    child_id: int
    age_months: int = Field(ge=0, le=60)
    weight_kg: float = Field(gt=0, le=40)
    height_cm: float = Field(gt=0, le=130)
    muac_cm: float = Field(gt=0, le=25)
    dietary_diversity: int = Field(ge=0, le=10, default=0)
    recent_illness: int = Field(ge=0, le=1, default=0)
