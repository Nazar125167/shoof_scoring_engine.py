from typing import Dict, List
from shoof_scoring_engine import ShoofTrustAgent # استيراد محرك الحساب الدقيق
# إنشاء مثيل لمشغل الحساب (يتم استيراد هذا مرة واحدة)
SCORING_ENGINE = ShoofTrustAgent()

def get_custom_weights(priority: str) -> Dict:
    """تعديل الأوزان لتعكس أولوية العميل"""
    # نبدأ بالأوزان الافتراضية
    base_weights = SCORING_ENGINE.trust_weights.copy()
    
    if priority == "جودة":
        # نزيد وزن الجودة والموثوقية ونقلل السعر
        base_weights['quality'] = 0.45  # زيادة
        base_weights['reliability'] = 0.30 # زيادة
        base_weights['price'] = 0.05    # تقليل
        base_weights['speed'] = 0.15 
        base_weights['extra'] = 0.05 
        
    elif priority == "سعر":
        # نزيد وزن السعر والسرعة
        base_weights['price'] = 0.35    # زيادة
        base_weights['speed'] = 0.30    # زيادة
        base_weights['quality'] = 0.15   # تقليل
        base_weights['reliability'] = 0.15
        base_weights['extra'] = 0.05
        
    # ملاحظة: مجموع الأوزان يجب أن يكون 1.0 (100%)
    return base_weights
